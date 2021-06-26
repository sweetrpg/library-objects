//
// Studio.swift
// Copyright (c) 2021 Paul Schifferer.
//

import Fluent
import Vapor


public final class Studio : Model {
    public static let schema = Studio.v20210625.schemaName

    @ID
    public var id : UUID?

    @Timestamp(key: Studio.v20210625.createdAt, on: .create)
    public var createdAt : Date?

    @Timestamp(key: Studio.v20210625.updatedAt, on: .update)
    public var updatedAt : Date?

    @Field(key: Studio.v20210625.name)
    public var name : String

    @Timestamp(key: Studio.v20210625.deletedAt, on: .delete)
    public var deletedAt : Date?

    public init() {
    }

    public init(id : UUID? = nil, name : String) {
        self.id = id
        self.name = name
    }

}

extension Studio : Content {}
