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
    
    @Siblings(through: VolumeAuthorPivot.self, from: \.$volume, to: \.$author)
    public var authors : [Author]

    @Siblings(through: VolumeStudioPivot.self, from: \.$volume, to: \.$studio)
    public var studios : [Studio]

    @Siblings(through: VolumePublisherPivot.self, from: \.$volume, to: \.$publisher)
    public var publishers : [Publisher]

    @Children(for: \.$volume)
    public var reviews : [Review]

    @Timestamp(key: Volume.v20210620.deletedAt, on: .delete)
    public var deletedAt : Date?

    public init() {
    }

    public init(id : UUID? = nil, name : String) {
        self.id = id
        self.name = name
    }

}

extension Volume : Content {}
