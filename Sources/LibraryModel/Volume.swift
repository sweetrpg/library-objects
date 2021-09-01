//
// Volume.swift
// Copyright (c) 2021 Paul Schifferer.
//

import Fluent
import Vapor


public final class Volume : Model {
    public static let schema = Volume.v20210620.schemaName

    @ID
    public var id : UUID?

    @Timestamp(key: Volume.v20210620.createdAt, on: .create)
    public var createdAt : Date?

    @Timestamp(key: Volume.v20210620.updatedAt, on: .update)
    public var updatedAt : Date?

    @Field(key: Volume.v20210620.name)
    public var name : String

    @Field(key: Volume.v20210620.slug)
    public var slug : String

    @Field(key: Volume.v20210620.isbn)
    public var isbn : String

    @Siblings(through: VolumeAuthorPivot.self, from: \.$volume, to: \.$author)
    public var authors : [Author]

    @Siblings(through: VolumeStudioPivot.self, from: \.$volume, to: \.$studio)
    public var studios : [Studio]

    @Siblings(through: VolumePublisherPivot.self, from: \.$volume, to: \.$publisher)
    public var publishers : [Publisher]

    @Siblings(through: VolumeTagPivot.self, from: \.$volume, to: \.$tag)
    public var tags : [Tag]

    @Parent(key: Volume.v20210625.systemId)
    public var system : LibraryModel.System

    @Children(for: \.$volume)
    public var reviews : [Review]

    @Children(for: \.$volume)
    public var properties : [VolumeProperty]

    @Timestamp(key: Volume.v20210620.deletedAt, on: .delete)
    public var deletedAt : Date?

    public init() {
    }

    public init(id : UUID? = nil, name : String, systemId : LibraryModel.System.IDValue) {
        self.id = id
        self.name = name
        self.$system.id = systemId
    }

}

extension Volume : Content {}
